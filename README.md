# Automation Project for Business Data Update

This project aims to automate the process of updating business data in a municipal system. Previously, the process involved extracting a spreadsheet with the company data, but there were often issues because the registration done by accountants did not always contain all the necessary information. Due to the General Data Protection Regulation (GDPR), it is not possible to require accountants to provide all the data, which led to a manual and time-consuming search for company contacts.

To solve this problem, we have developed a program capable of automating the data extraction process using a static website and the BeautifulSoup library for web scraping. This allows us to update the company data quickly, efficiently, and at scale.

## How to Use the Program

### Prerequisites
- Installed Python 3.x
- Installed Git

### Cloning the Repository

1.Open your operating system terminal.

2.Navigate to the directory where you want to clone the repository.

3.Execute the following command to clone the repository:

`git clone https://github.com/GustavoMalimpensa/atualizando_dados`


### Installing Dependencies

1. Navigate to the cloned project directory:

`cd atualizando_dados`


2. Execute the following command to install the required libraries:

`pip install -r requirements.txt`


This will install the following Python libraries:

- os
- requests
- BeautifulSoup
- json
- urllib

### Running the Program

1.Open the tratativa.py file in a text editor.

2.Verify that the paths for the resultados.json and empresas.json files are correct. If necessary, adjust the paths to match the structure of your project.

3.Execute the program:

`python tratativa.py` 

The program will start the data extraction process and create the resultados.json file in the resultados folder. The results will be saved in this 

## Contribution

Contributions are welcome! If you would like to contribute to this project, follow the steps below:

1.Fork the repository.
2.Create a new branch with your contribution: git checkout -b my-contribution.
3.Make the desired changes.
4.Commit your changes: git commit -m 'My contribution'.
5.Push your changes to the remote repository: git push origin my-contribution.
6.Open a pull request in the original repository.

## License

And of course:

MIT: https://rem.mit-license.org



