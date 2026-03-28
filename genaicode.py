from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<style>
body { font-family: Arial; background:#f4f6f8; padding:20px; }
.container { background:#fff; padding:20px; border-radius:10px; max-width:900px; margin:auto; }
input { padding:8px; margin:5px; }
button { padding:10px; margin-top:10px; background:#0d6efd; color:white; border:none; cursor:pointer; }

.table { width:100%; border-collapse:collapse; margin-top:20px; }
.table td, .table th { border:1px solid #ddd; padding:10px; }

.high { background:#f8d7da; }
.medium { background:#fff3cd; }
.low { background:#d4edda; }

.tips { margin-top:20px; padding:15px; background:#e2eafc; border-radius:8px; }
</style>
</head>
<body>

<div class="container">
<h1>📚 Personalized Study Plan Generator</h1>

<h3>Enter Marks (Out of 70)</h3>
DLCO: <input type="number" id="dlco" max="70"><br>
MEFA: <input type="number" id="mefa" max="70"><br>
ADSA: <input type="number" id="adsa" max="70"><br>
IDS: <input type="number" id="ids" max="70"><br>

<h3>Available Study Hours</h3>
<input type="number" id="hours"><br>

<button onclick="generatePlan()">Generate Plan</button>

<div id="output"></div>
</div>

<script>
function getPriority(mark){
 if(mark > 70) mark = 70;
 if(mark < 0) mark = 0;

 if(mark >= 55) return {level:"High", class:"low", weight:3};
 if(mark >= 35) return {level:"Medium", class:"medium", weight:2};
 return {level:"Low", class:"high", weight:1};
}

function generatePlan(){

 let subjects=[
  {name:"DLCO", mark:+document.getElementById("dlco").value},
  {name:"MEFA", mark:+document.getElementById("mefa").value},
  {name:"ADSA", mark:+document.getElementById("adsa").value},
  {name:"IDS", mark:+document.getElementById("ids").value}
 ];

 let hours=+document.getElementById("hours").value;

 if(!hours){
  alert("Enter study hours");
  return;
 }

 let totalWeight=0;

 subjects.forEach(s=>{
  let p=getPriority(s.mark);
  s.priority=p.level;
  s.class=p.class;
  s.weight=p.weight;
  totalWeight+=p.weight;
 });

 let html="<h2>Personalized Study Plan</h2>";
 html+="<table class='table'>";
 html+="<tr><th>Priority</th><th>Subject</th><th>Marks</th><th>Hours</th><th>Strategy</th></tr>";

 subjects.forEach(s=>{
  let hrs=((s.weight/totalWeight)*hours).toFixed(1);

  let tip="";
  if(s.weight==3)
    tip="Maintain performance.";
  else if(s.weight==2)
    tip="Revise regularly.";
  else
    tip="Focus on basics.";

  html+=`<tr class="${s.class}">
  <td>${s.priority}</td>
  <td>${s.name}</td>
  <td>${s.mark}/70</td>
  <td>${hrs}</td>
  <td>${tip}</td>
  </tr>`;
 });

 html+="</table>";

 html+=`<div class="tips">
 <h3>💡 General Study Tips</h3>
 <ul>
 <li>Take short breaks</li>
 <li>Follow routine</li>
 <li>Avoid distractions</li>
 </ul>
 </div>`;

 document.getElementById("output").innerHTML=html;
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)