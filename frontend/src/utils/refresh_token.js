import axios from "axios";


async function refreshAccessToken(username) {
    console.log("getting refresh token")
    // Get the refresh token from local storage
    let refresh_token = localStorage.getItem(`refresh_token_${username}`);

    // Set the Authorization header of the axios instance
    axios.defaults.headers.common["Authorization"] = "Bearer " + refresh_token;

    await axios.post("http://127.0.0.1:5000/api/token/refresh")
    .then((res) => {
        let n_access_token = res.data.access_token;
        console.log(n_access_token)

        localStorage.setItem(`access_token_${username}`, n_access_token);

        axios.defaults.headers.common["Authorization"] = "Bearer " + n_access_token;

        return "success"

    }).catch((rej) => {
        // console.log(rej)
        alert("Please Login Again")
        return "unsuccess"
    })
        
    
}

export default refreshAccessToken;