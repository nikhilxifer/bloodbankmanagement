<script type="text/javascript">
  
function d(x1,x2){
 var x1 = document.getElementById('x1');
 var x2 = document.getElementById('x2');

 x2.innerHTML = "";

 if (x1.value == "Himachal Pradesh") {

  var oparray = ['shimal|Shimla','una|Una','kinnaur|Kinnaur'];
 }

 elseif(x1.value == "Punjab"){
  var oparray = ['opgg|Ludhiana','sdfd|karnal']
 }

 for (var o in oparray){
    var pair = oparray[o].split("|");
    var newo = document.createElement("o");

    newo.value = pair[0];
    newo.innerHTML = pair[1];
    x2.o.add(o);
 }

}
   </script>