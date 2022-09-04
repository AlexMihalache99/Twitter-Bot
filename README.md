# Twitter-Bot


I created Twitter bots for my personal account at https://twitter.com/freelancerchamp.
I used the Twitter Developer API. It can be accessed by creating an account at https://developer.twitter.com.

I have designed three separate bots that run simultaneously:
 - bot that creates tweets.
 - bot that likes tweets.
 - bot that retweets tweets.
 
 <h2>TwitterCreate</h2>
Inside the quotes_all.csv file there are different types of quotes by important people through time.
 
Using panda I read the csv file and iterate through it row by row.<br>

Apart from the csv file index, I have a separate one that I write on a file called tweet_index.txt.
Whenever the bots creates a tweet, it updates the index and overwrite the tweet_index file, such that if I stop the program and rerun, it will start from where it was left, instead of starting from the beginning everytime.<br>

Checks if the tweet is smaller than 280 characters(twitter limit) and create the tweet using the **api.update_status** command. Then a time sleep of 6 hours between each tweet is applied.

<h2>TwitterLike</h2>

I have a search array that contains random words from the programming lexicography.<br>

Then generates a random word from that array. Loops through all the tweets that contain the random word. Checks if its mine or if it has been liked previously.<br>

If it was not, then checks the tweet score using **TextBloB**. If the score is higher than 0.5, then the bots likes the tweet.<br> 
This cycle is repeated infinitely such that every 10 tweets, the random word changes. After the bot liked one tweet, a delay of 6 minutes is applied.

<h2>TwitterRetweet</h2>
I have a search array that contains random words from the programming lexicography.<br>

Then generates a random word from that array. Loops through all the tweets that contain the random word. Checks if its mine or if it has been retweeted previously.<br>

If it was not, then checks the tweet score using **TextBloB**. If the score is higher than 0.5, then the bots reteets the tweet.<br> 
This cycle is repeated infinitely such that every 10 tweets, the random word changes. After the bot retweeted one tweet, a delay of 6 hours is applied.
 

 
 
