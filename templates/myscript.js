

function foo(){
    alert('hello');
}




//var test_menu = document.getElementById("test_menu");
//test_menu.onchange = function(){
function select_menu(){
  var test_menu = document.getElementById("test_menu");
  var chosen_test = test_menu.options[test_menu.selectedIndex];
  switch (chosen_test.text){
    case "Main Main":
      checkAll(document.checkbox.to_run);
      break;
    case "Main Short":
      checkspecific(document.checkbox.to_run, "Main Short");
      break;
    case "Smoke":
      checkspecific(document.checkbox.to_run, "Smoke");
      break;
    default:
      uncheckAll(document.checkbox.to_run);
      break;
  }
}

function checkspecific(field, test_type){
uncheckAll(field);
switch (test_type){
  case "Smoke":
    main_actions = new Array("1", "2", "3", "4", "5", "6", "8",  "21", "22", "23", "35", "38", "67");
    break;
  case "Main Short":
    main_actions = new Array(1, 2, 3, 4, 5, 6, 8, 9, 12, 13, 14, 15, \
    16, 17, 18, 20, 21, 22, 23, 27, 28, 29, 30, 31, 32, 33, 37, 38, 39, \
    45, 46, 47, 49, 53, 55, 56, 58, 62, 63, 64, 65, 67, 68, 69, 70, 74, 75, 77, 79);
    break;
  default:
    main_actions = new Array();
    break;
}
for (key in main_actions){
   for (i = 0; i <field.length; i++){
      action_num = main_actions[key];
      if (field[i].value == action_num)
	 field[i].checked = true;
      }
   }
}

function uncheckAll(field){
for (i=0;i<field.length; i++)
	field[i].checked = false;
}
function checkAll(field){
for (i=0; i < field.length; i++)
	      field[i].checked = true;

}