//Chooses to Kick, ban, or kick all users
function ChoiceFunc(){
	switch (document.getElementById("Command_Selection").value){
		case "kick":
			document.getElementsByName('output')[0].value= document.getElementsByName('user')[0].value + " has been kicked";
			document.getElementsByName('user')[0].value='';
			break;
		case "ban":
			document.getElementsByName('output')[0].value= document.getElementsByName('user')[0].value + " has been banned";
			document.getElementsByName('user')[0].value='';
			break;
		case "kickall":
			document.getElementsByName('output')[0].value= "All users have been kicked";
			document.getElementsByName('user')[0].value='';
			break;
		default:
			window.alert("NOT WORKING");
			break;
	}
}