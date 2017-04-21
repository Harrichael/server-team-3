//Chooses to Kick, ban, or kick all users

var commands = ['kick','ban','kickall','UserList','ServerStatus','ServerShutdown','CreateRoom','DeleteRoom','Whitelist','Blacklist','UnBan','CommandList'];

function ChoiceFunc(){
	switch (document.getElementById('Command_Selection').value){
		case commands[0]:
			document.getElementsByName('output')[0].value= document.getElementsByName('user')[0].value + " has been kicked";
			document.getElementsByName('user')[0].value='';
			break;
		case commands[1]:
			document.getElementsByName('output')[0].value= document.getElementsByName('user')[0].value + " has been banned";
			document.getElementsByName('user')[0].value='';
			break;
		case commands[2]:
			document.getElementsByName('output')[0].value= "All users have been kicked";
			document.getElementsByName('user')[0].value='';
			break;
		default:
			window.alert("NOT WORKING");
			break;
	}
}

function CommandLine(){
	switch (document.getElementById('command').value){
		case commands[3]:
			document.getElementsByName('output')[0].value= "List of Users";
			document.getElementsByName('command')[0].value='';
			break;
		case commands[4]:
			document.getElementsByName('output')[0].value= "Server Diagnostics";
			document.getElementsByName('command')[0].value='';
			break;
		case commands[5]:
			document.getElementsByName('output')[0].value= "Shutdown Server";
			document.getElementsByName('command')[0].value='';
			break;
		case commands[6]:
			document.getElementsByName('output')[0].value= "Create New Room";
			document.getElementsByName('command')[0].value='';
			break;
		case commands[7]:
			document.getElementsByName('output')[0].value= "Delete a Room";
			document.getElementsByName('command')[0].value='';
			break;
		case commands[8]:
			document.getElementsByName('output')[0].value= "Whitelist for Current Room (If Applicable)";
			document.getElementsByName('command')[0].value='';
			break;
		case commands[9]:
			document.getElementsByName('output')[0].value= "Blacklist of Current Room (If Applicable)";
			document.getElementsByName('command')[0].value='';
			break;
		case commands[10]:
			document.getElementsByName('output')[0].value= "UnBan a User";
			document.getElementsByName('command')[0].value='';
			break;
		case commands[11]:
			document.getElementsByName('output')[0].value= "Commands: " + commands.join(' - ');
			document.getElementsByName('command')[0].value='';
			break;
		default:
			window.alert("INVALID COMMAND");
	}
}

function handle(e){
	if(e.keyCode === 13){
            e.preventDefault();
			CommandLine();
    }
}

$.ajax({
  type: "POST",
  url: "/api/users",
  data: {"username":"test","password":"pass","email":"test"},
  success: function (data, textStatus, xhr) {
	  alert("It Worked");
  } ,
  contentType: "application/json",
  dataType: "json"
});

