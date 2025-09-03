## Download the required model for semantic search
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')
embeddings = model.encode(sentences)
print(embeddings)

## Download dependencises
! git clone https://github.com/cyberytti/ToolHunt

!pip install pyngrok langchain langchain-huggingface langchain-community faiss-cpu rank_bm25


# =========================
# Directly Run ToolHunt in Colab (Debugging Mode)
# =========================

import os
import sys
import threading
import time
from pyngrok import ngrok

# --- 1. Set up paths and environment ---
project_root = "/content" # Standard Colab working directory
toolhunt_dir = os.path.join(project_root, "ToolHunt")

if not os.path.isdir(toolhunt_dir):
    raise FileNotFoundError(f"ToolHunt directory not found at {toolhunt_dir}")

# Crucially, add the project root to Python's path
# This allows 'from backend.main import ...' to work when app.py is run
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    print(f"Added {project_root} to sys.path")

print(f"Project root: {project_root}")
print(f"ToolHunt dir: {toolhunt_dir}")
print(f"sys.path (relevant parts): {[p for p in sys.path if 'content' in p]}")

# Set ngrok token
ngrok.set_auth_token('Your ngrok authentication key')

# --- 2. Import and run Flask app ---
try:
    # Change working directory to ToolHunt so relative paths inside app.py work
    # (like loading templates)
    os.chdir(toolhunt_dir)
    print(f"Changed working directory to: {os.getcwd()}")

    # Now we can import app.py as a module because we added /content to sys.path
    # and we are running from within the ToolHunt directory for relative file paths.
    import app

    print("✅ Successfully imported app.py")

    # --- 3. Run Flask in a separate thread ---
    def run_flask():
        print("🚀 Starting Flask app...")
        # Run Flask app. Note: debug=True might cause issues in threads/Colab,
        # but let's try it first. If problems occur, remove debug=True.
        app.app.run(host='127.0.0.1', port=5000, debug=False) # Start without debug first

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True # Dies when main thread dies
    flask_thread.start()
    print("🧵 Flask thread started.")

    # --- 4. Wait and check ---
    # Give Flask time to start (especially for model download on first run)
    print("⏳ Waiting for Flask to initialize...")
    time.sleep(8) # Adjust if needed

    # A simple check if the thread is still alive (not a guarantee the server is up)
    if flask_thread.is_alive():
        print("✅ Flask thread is running.")
    else:
        print("⚠️ Flask thread has stopped. Check for errors in the logs above.")

    # --- 5. Create ngrok tunnel ---
    print("🚇 Starting ngrok tunnel...")
    tunnel = ngrok.connect(5000, "http")
    print("\n🎉 ToolHunt is ready!")
    print(f"🔗 Public URL: {tunnel.public_url}")
    print("\nPress the 'Interrupt Execution' button (⏹️) in Colab to stop.")

    # --- 6. Keep alive ---
    # Keep the main thread alive to maintain the tunnel
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Interrupted by user.")
    finally:
        print("🧹 Cleaning up...")
        ngrok.kill()
        # Note: Stopping the Flask thread cleanly from here is tricky in Colab.
        # The daemon thread will stop when the main program ends.
        print("✅ Done.")

except Exception as e:
    print(f"❌ An error occurred during startup: {e}")
    import traceback
    traceback.print_exc()
