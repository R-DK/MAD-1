function validate(event){
	v = document.getElementById("email").value;
	if(v.indexOf("@") == -1){
		event.preventDefault();
		alert("Enter a valid email")
		return false;
	}
	return true;
}

function create(article, response){
	var div = document.createElement('div');
	div.className = "message";
	div.innerHTML = "Thank you for liking";
	article.parentNode.appendChild(div);
}

function send_like(event){
	article= event.target;
	article_id = article.dataset.article_id;
	fetch('/article/'+article_id).then(
		response => create(article, response)
	).catch(
		err => console.log(err)
	)
}

function initialize(){
	like_buttons = document.querySelectorAll(".like-icon");
	for(const like_button of like_buttons){
		like_button.onclick = send_like;
	}
}