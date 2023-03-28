[01/03 9:41 pm] Pandey, Kavyansh




BlockChain and Web3.0




Cryptography based data transfer

Central validation Mechanism

Permanent record (immutable)

Secure, anonyms and immutable records




Web2.0 has single point of failure(SPOF), web3.0 overcome with this(decentralized and one to one, No third party intervention)




Working of blockchain -

miners solved complex mathematical puzzles in order to create next block. After solving puzzles they have access to create new block.




Transaction in web2.0 vs web3.0

transfer of payment in web2.0 requires bank subsidiary, third party in order to transfer money from source to destination while in web3.0 direct transfer happened (peer to peer), avoid SPOF. Web3.0 is all about eliminating and reducing SPOF with decentralisation.




encryption generally avoids the reverse engineering of data (used in web3.0)


Algorithms used for encryption -

Symmetric Encryption, Asymmetric encryption, Hashing




Semantic web - data can been read and understand by machine, machine readable




NFT -

Non Fungible (Irreplaceable, immutable ) Token.
It can be a digital form of an art of work, a house an image anything.
Each NFT is associate with one user and all users connected via a blockchain network.
Since all users connected over a blockchain network, there is transparency for each an every transaction, who is buying and who is selling their NFTs.
prices for buying and selling generally in the form of digital currency (eq, bitcoin).



Tech Stack -

Front end can be any FE framwork like react or vueJS.

For creating block chain network, smart contract, Solidity (hardhat- help solidity run locally) can be used.

 




MetaVerse




Application - Minecraft, Fortnite (Attending events)


Involve 3D programming - Unreal Engine, Unity

Super Computing, Like Tesla using Environment and running machine learning models there (Auto Pilot in Tesla)

Media and Entertainment - Marvel (Villain Animations are 3d programming in Unity)

AR VR Experience - Tiktok, Snapchat, Insta Filters




Use cases -

Virtual Meetings in meta worlds
VR AR in selecting Products
Purchasing and selling goods in metaverse in exchange of digital currency.




Tech Stack -

3d programming - Unreal Enginer- C++, Unity #
framwork - three.js, babylon.js
AWS services - AWS appstream 2.0(for 3 apps), AWS sumerain (for AR VR applications), speed 3d on AWS





[02/03 11:09 pm] Pandey, Kavyansh




Recommendation System -




Use case -

You are purchasing an iphone on amazon or any e-commerce, and got recommandations like, airpods or buy this too.
Watching series on Netflix for example - you watch GOT, got recommendation for vikings and House of dragons (Same type series).
Searching a product on a platform, getting recommendation on social network sites like insta or facebook.


Two type of recommendation system -

Content based filtering system
Collaborative filtering




Content Based - (Amazon, Flipkart)

Example of moveis, every movies has generes like action, horror, comedy.

Suppose user 1 watch horror movies, action movie, and given some ratings.

User2 watch an action movie and give a similar rating to the movie, there will much probability that user2 will also get recommendation for Horror movie too.




Collaborative filtering - (Netflix, Amazon prime)

Instead of rating, more focus on user behaviour, if user watch m1, m2 and m3 movie so user2 also get recommendation for those movies since characteristics of both user quite similar.




Tech Stack -

Python, R

libraries - scikit-surprise, tenserflow-recommenders, recmetrics (some general libraries to work with datasets, pandas and numpy)

AWS Sagemaker (notebooks, training algorithms, hosting services), AZURE ML and GoogleCloud ML.






Mostly this will be done on FE side. I can't see any BE work on this functionality.

 

Solution

 

We have some modules in Javascript like voiceToText, this can be easily integrated with Angular application.

 

We can do the following.

Take inputs as per user voice
Decide some keywords like Wickets, Extra's, Runs, Wide etc for specific actions.
Use a word like Stop/Done or a Pause, that will check one score is Done, Now take input for second score.
create specific payload(Data needs to send to BE) for each actions (Wide, extra, run, Wicket). And on the basis of check respected data should be send with player details.
Make websocket call after Stop or Pause.

We need to make some commands for each actions that will execute if any specific word found in text.
Some example commands -
Change batsman Striker as Player Name Done
Edit details over 4 delivery 3 Stop Done


