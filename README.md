# 🖱️ Auto Clicker Python
Auto clicker script useful for automatization.

## Installation
Clone the [github](https://github.com/noValve/auto-clicker-python) repository.

```bash
git clone git@github.com:noValve/auto_clicker-python.git
```

## Usage
```bash
# Place yourself inside the project folder
cd auto-clicker-python

# Run the script
python3 auto_clicker.py
```

Run the autoclicker using <kbd>F1</kbd>.  
Pause the autoclicker using <kbd>F2</kbd>.  
Exit using <kbd>F3</kbd>.

## Settings

In order to change the settings such as the <strong>number of clicks per second</strong>, the <strong>keys</strong> used to <strong>run</strong>, <strong>pause</strong> and <strong>exit</strong> the script, change the following lines in <strong><code>auto_clicker.py</code></strong>.

```py
# ======= Settings =======
run_key = Key.f1
pause_key = Key.f2
exit_key = Key.f3
click_delay = 0.05 # delay between each click (in seconds)
```  

## License

⚖️ [MIT](https://choosealicense.com/licenses/mit/)
