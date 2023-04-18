function attachEvents() {
    const POSTS_URL = "http://localhost:3030/jsonstore/blog/posts";
    const COMMENTS_URL = "http://localhost:3030/jsonstore/blog/comments";

    const buttonLoadPosts = document.getElementById("btnLoadPosts");
    buttonLoadPosts.addEventListener("click", loadPosts);
    const buttonViewPosts = document.getElementById("btnViewPost");
    buttonViewPosts.addEventListener("click", viewPosts);

    let postDetails = null;
    let postHeader = null;
    let postID = null;

    async function loadPosts(){
        let postData = await fetch(POSTS_URL);
        postData = await postData.json();
        const selectDropDown = document.getElementById("posts");

        for (const key in postData) {
            let dropDownOption = document.createElement("option");
            dropDownOption.value = key;
            dropDownOption.textContent = postData[key]["title"];
            postDetails = postData[key]["body"];
            postHeader = postData[key]["title"];
            selectDropDown.appendChild(dropDownOption);
        }

    }

    async function viewPosts(){

        const userSelectedOption = document.getElementById("posts");
        const selectedOptionKey = userSelectedOption.value;

        let postData = await fetch(POSTS_URL);
        postData = await postData.json();

        postDetails = postData[selectedOptionKey]["body"];
        postHeader = postData[selectedOptionKey]["title"];
        postID = postData[selectedOptionKey]["id"];

        const titleSection = document.getElementById("post-title");
        titleSection.textContent = postHeader;

        const paragraphSection = document.getElementById("post-body");
        paragraphSection.textContent = postDetails;


        const ulCommentSection = document.getElementById("post-comments");
        ulCommentSection.innerHTML = ""

        let commentData = await fetch(COMMENTS_URL);
        commentData = await commentData.json();

        for (const key in commentData) {
            if (commentData[key]["postId"] === postID) {
                let comment = document.createElement("li");
                comment.textContent = commentData[key]["text"];
                ulCommentSection.appendChild(comment);
            }
        }

    }

}

attachEvents();