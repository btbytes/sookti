<html>
<head>
<title>
Test Page:Quote
</title>
<style type="text/css">
body{
  background: #669;
  font-family:verdana;
}
div#container{
  margin:7em auto;
  width: 600px;
}
div#container h1{
  margin:0px;
  margin-bottom:-5px;
  color: #ff9;
  text-align:center;
}
div#quote{
  border: solid 3px #944;
  padding: 1em;
  background: #fff;
}
div#quote h2{
   margin:0px;
   border-bottom:solid 1px #999;
   margin-bottom: 1em;   
}
</style>
</head>

<body>
<div id="container">
<h1>Q Server</h1>
<div id="quote">
${ next.body()}
</div>
</div><!-- container -->
</body>
</html>