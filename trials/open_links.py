import webbrowser
import time

# Settings
file_path = "reopen.txt"       # path to your .txt file
batch_size = 5                # how many links to open at once
delay_between_batches = 10    # seconds to wait between batches

# Load links
with open(file_path, "r", encoding="utf-8") as f:
    links = [line.strip() for line in f if line.strip()]

# Open links in batches
for i in range(0, len(links), batch_size):
    batch = links[i:i + batch_size]
    for link in batch:
        webbrowser.open_new_tab(link)  # open in new tab
        time.sleep(1)  # slight delay between each link (optional)

    print(f"Opened batch {i // batch_size + 1} of {len(links) // batch_size + 1}")
    time.sleep(delay_between_batches)

