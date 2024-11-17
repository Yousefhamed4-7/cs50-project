let select = document.querySelector("form select");
let mcq = document.querySelector(".MCQ");
let tf = document.querySelector(".TF");

function hideall() {
  mcq.style.display = "none";
  tf.style.display = "none";
}
hideall();
tf.style.display = "block";

select.onchange = () => {
  hideall();
  document.querySelector(`.${select.value}`).style.display = "block";
};