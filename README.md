# 🕵️‍♂️ Proxy Checker

This Python script checks if a list of proxies is working or not by making a request to a website. If the proxy is working, it will be added to the `good.txt` file.

## 🚀 Getting Started

To get started with this script, you'll need to follow these steps:

1. Clone the repository.
2. Install the necessary dependencies (`requests`).
3. Run the script using `python proxy_checker.py`.

That's it! 🎉 The script will automatically check the proxies for you and add the working ones to the `good.txt` file.

## ✔️ Fresh, Checked Proxies

If you're looking for fresh, checked proxies to use, look no further than the [good.txt](https://github.com/Bardiafa/Proxy-Checker/blob/main/good.txt) file in this repository. These proxies have been recently checked and confirmed to be working.

## 🧐 How It Works

The script uses the `requests` library to make requests to a website using a given proxy. If the website returns a 200 status code, the script assumes that the proxy is working and adds it to the `good.txt` file.

The script uses multiple threads to check the proxies concurrently, which can speed up the process significantly.

## 🤖 Automation

You can automate the running of this script using GitHub Actions. Simply create a new workflow in your repository and use the provided YAML file to run the script on every push to the main branch.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Bardiafa/Proxy-Checker/blob/main/LICENSE) file for details.

## 👨‍💻 Author

This script was created by [Me](https://github.com/Bardiafa) & [Hossein](https://github.com/hossein-mohseni) in Collaboration in our Wonderful Team [Mizegerd.tech](https://github.com/mizegerd-tech). If you have any questions or suggestions, please feel free to contact us in [Issues](https://github.com/Bardiafa/Proxy-Checker/issues) Part!
