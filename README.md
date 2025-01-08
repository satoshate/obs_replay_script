# OBS Auto Replay Saver and Restarter

This OBS Studio script automatically saves the current replay buffer and restarts it with a single hotkey press. This is useful for quickly capturing highlights and ensuring the replay buffer is always ready for the next moment.

## Features

* **Hotkey Activated Saving:** Save your replay buffer instantly by pressing a configured hotkey.
* **Automatic Replay Buffer Start:** If the replay buffer is not active, the script attempts to start it automatically.
* **Automatic Restart After Save:** After a successful save, the script automatically restarts the replay buffer, ensuring you don't miss the next highlight.
* **Error Handling and Logging:** Provides logging information in the OBS Studio logs to help diagnose any issues.
* **Handles Inactive Buffer:** Gracefully manages scenarios where the replay buffer is not running.
* **Simple Setup:** Easy to install and configure within OBS Studio.

## How to Use

1. **Download the Script:** Download the `script.py` file.
2. **Open OBS Studio:** Launch OBS Studio.
3. **Go to Scripts:** In OBS Studio, navigate to `Tools` -> `Scripts`.
4. **Add the Script:** Click the "+" button at the bottom of the Scripts window and select the downloaded `script.py` file.
5. **Configure Hotkey:**
   * Go to `Settings` -> `Hotkeys`.
   * Search for the action named "Save and restart replay buffer" (under the "Scripts" section).
   * Assign your desired hotkey to this action.
6. **Close the Scripts Window:** You are now ready to use the script.

## Why This Script?

Manually saving the replay buffer and then remembering to restart it can be cumbersome and can lead to missing important moments. This script streamlines this process by combining both actions into a single hotkey press, ensuring you never miss a highlight while also keeping your replay buffer active.

## Configuration

The script requires you to assign a hotkey to the "Save and restart replay buffer" action in the OBS Studio hotkey settings. This hotkey will trigger the script's functionality.

## Potential Issues and Considerations

* **Replay Buffer Configuration:** Ensure your replay buffer is correctly configured in OBS Studio settings (under "Output").
* **Storage Location:** The saved replays will be stored in the directory specified in your OBS Studio output settings.
* **Error Logs:** Check the OBS Studio logs (`Help` -> `Log Files` -> `Show Log Files`) if you encounter any issues. The script provides logging information that can be helpful for troubleshooting.

## Contributing

Feel free to submit pull requests for improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).
