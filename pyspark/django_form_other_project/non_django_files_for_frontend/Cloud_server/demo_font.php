












<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Number Converter</title>
  <!-- bootstrap link start -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
    integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
    integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
    integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  <!-- bootstrap link end -->
  <style>
    .themainbutton{
      min-width: 220px;
    }
  </style>
</head>

<body style="background-color: #24222a;">
       </br>
  <div class="container ">

    <div class=" d-flex justify-content-center">
      <label for="uname" class="text-white justify-content-center">Number Converter</label>
       </div>
        </br>

    <div class=" d-flex justify-content-center">
      <form action=""  method="post" class="mt-3">


        <div class="form-group" id ="value">
              <label for="uname" class="text-white">Enter a Number</label>
              <input type="text" class="form-control" id="Number" name="uname" placeholder="Number"  value="">
              <label for="uname" class="text-white">Number:</label>
              <div id ="changer">

              </div>
        </div>




        
        
      </form>


    </div>
    <div class=" d-flex justify-content-center">
     <button type="submit" class="btn btn-primary" onclick="getInputValue();" value="Submit">Submit</button>
   </div>
</div>



<script>



function post_responce(path,func,varible){

  console.log(path);
  fetch(path).then(
      ( response) => {
          return response.text();
      })
      .then((html) => {
          func(  html.trim()  , varible )
      });



}

function change(value){


          document.getElementById("changer").innerHTML = "<div id =\"changer\">    <label for=\"uname\" class=\"text-white\">"+value+"</label> </div> ";

}

//http://alexhaussmann.com/adhaussmann/a_final/decode_from_Pi.php?number=1

      function getInputValue() {
        // Selecting the input element and get its value 
        var inputVal = document.getElementById("Number").value;
        // Displaying the value
        //alert(inputVal);
        document.getElementById("changer").innerHTML = "<div id =\"changer\">    <label for=\"uname\" class=\"text-white\">Loadings</label> </div> ";

        post_responce("http://alexhaussmann.com/adhaussmann/a_final/decode_from_Pi.php?number="+inputVal,change,"");



      }



</script>


