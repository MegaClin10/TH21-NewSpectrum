async function getTopicArticles(topic="Donald", sourceBias = 0, authorBias = 0){
    let url = "https://aqueous-wave-82169.herokuapp.com/article/?q=" + topic;
    console.log(url)
    
    fetch(url)
    .then(result => result.json())
    .then((data) => {
        for(let i = 0; i < data.length; i++){
            console.log(data.length);
        }
        console.log(data);
    });
}

getTopicArticles();


