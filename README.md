# GPU Memory Alert

`gpu-memory-alert` is a tool to monitor GPU memory usage on a multi-GPU system using `gpustat`. If any GPU's memory usage drops below a specified threshold, an email notification will be sent.

## Installation

Follow these steps to install and set up the tool.

### 1. **Install the package**:

You can install the package from PyPI using `pip`:

```bash
pip install gpu-memory-alert
```

Alternatively, you can clone this repository and install the package locally:

```bash
git clone https://github.com/yourusername/gpu-memory-alert.git
cd gpu-memory-alert
pip install .
```

### 2. **Install required dependencies**:

Make sure you have the necessary dependencies installed, such as `gpustat` for GPU monitoring and `jq` for JSON parsing.

- Install `gpustat`:

  ```bash
  pip install gpustat
  ```

- Install `jq` (for JSON parsing). On Ubuntu, you can install it using:

  ```bash
  sudo apt-get install jq
  ```

  On macOS, you can use `brew`:

  ```bash
  brew install jq
  ```

### 3. **Configure the tool**:

Before running the script, you need to configure the GPU memory threshold and email recipient.

1. **Edit the configuration file (`config/thresholds.conf`)**:

   Open the file `config/thresholds.conf` and set the memory threshold (in MiB) and the email address to receive alerts.

   Example:

   ```bash
   MEMORY_THRESHOLD=1024   # Set the memory threshold in MiB (1 GB)
   EMAIL_RECIPIENT=your_email@example.com
   ```

   - **`MEMORY_THRESHOLD`**: This is the threshold for GPU memory usage. If any GPU's memory usage falls below this value, an email notification will be sent.
   - **`EMAIL_RECIPIENT`**: This is the email address where you want to receive alerts.

2. **Optional: Configure Email**:

   If you're using `mail` to send notifications, ensure your system is configured to send emails. You can use services like **`sendmail`**, **`Postfix`**, or an SMTP relay. 

   Example configuration for `mail` (on Ubuntu):
   
   ```bash
   sudo apt-get install mailutils
   ```

### 4. **Running the script manually**:

To run the GPU memory monitoring script manually, execute the following command:

```bash
gpu-memory-alert
```

This will monitor all GPUs, and if any GPU's memory usage falls below the threshold, an email notification will be sent.
This is one time runner, if the threshold you set is satisfied, a notification will be sent and the program ends.

Alternatively, you can run the monitoring script directly using the shell:

```bash
bash scripts/gpu_memory_notify.sh
```

### 5. **Automating the script with cron**:

You can set up a **cron job** to run the script periodically (e.g., every minute) to automatically monitor the GPU memory and send alerts.

1. Edit your cron jobs:

   ```bash
   crontab -e
   ```

2. Add a cron job to run the script every minute:

   ```bash
   * * * * * /path/to/gpu-memory-alert/scripts/gpu_memory_notify.sh
   ```

   This will run the script every minute, check the GPU memory usage, and send email alerts if the memory falls below the specified threshold.

### 6. **Log file**:

The script logs its activity in the `logs/gpu_monitor.log` file. You can check this log to track the status of GPU memory checks and notifications.

```bash
tail -f logs/gpu_monitor.log
```

This will show the latest entries in the log file in real-time.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.