# Item Catalog Project
* This application provides a list categories and items as well as a user authentication system. Users will have the ability to add, edit and delete their own items. The project was developed using the Flask framework as well as OAuth2 to provides authentication.


## Code dependencies:
You must install the following to run the project
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [VM configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)

### How to Run the Project: 
* cd to the downloaded folder directory 
* run `vagrant up` to bring the virtual machine online 
* run `vagrant ssh` to log into the virtual machine 
* type `cd /vagrant` to change directory into vagrant directory 
* run  `python database_setup.py` to setup application database
* run `python database_init.py` to add categories items to the database
* run the command `python project.py` 
* Access the application locally in your Web Browser using [this link](http://localhost:5000/)


### JSON Endpoints
* Catalog JSON: /catalog/JSON - Displays the Categories 
* Categories JSON: /catalog/<path:categories_id>/JSON - Displays items of particular category 
* Category Items JSON: /catalog/<path:categories_id>/<path:items_id>/JSON - Displays a specific category item


## Acknowledgments
* Books icon from [iconfinder](https://www.flaticon.com/free-icon/book-shelf_1236517#term=library&page=1&position=46).
