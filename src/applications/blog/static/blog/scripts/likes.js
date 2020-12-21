
const like_color = function () {

    let api_url = "/blog/post/like_color/";

    fetch(api_url, {
        method: "POST",
    }).then(
        resp => {
            resp.json().then(
                resp_payload => {
                    if (resp_payload.ok) {
                        let posts_id = resp_payload.posts_id

                        for(let i = 0; i < posts_id.length; ++i){
                            let elem = document.getElementById("post_" + posts_id[i]);
                            elem.classList.add("like_red");
                        }
                    } else {
                        console.log(JSON.stringify(resp_payload));
                    }
                }
            );
        }
    );
}