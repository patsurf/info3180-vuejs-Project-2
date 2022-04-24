<script>
export default {
    data() {
        return {
            message: "Buy and Sell Car Online"
        };
    },
}
</script>

<template>
    <div class="container">
      <img alt="Car logo" class="logo" src="uploads\photo-1542282088-fe8426682b8f.jfif"/>
      <div class="Herotext">
        <h1>Buy and Sell Cars Online</h1> 
        <p>United Auto Sales provides the fastest, easiest and most user friendly way to buy or sell cars online. Find a  Great Price on the Vehicle You Want</p>    
      </div>
    </div>
</template>

<style>
/* Add any component specific styles here */
  body {
    background-color: #fff;
  }
  .Herotext {
    inline-size: 400px;
    position: absolute;
    top: 50%;
    transform: translate(0, -50%);
    padding: 10px;
  }
  .Herotext h1 {
    font-size: 50px;
    font-weight: bold;
    color: #005888;
    padding-bottom: 15px;

  }
  .Herotext p {
    font-size: 20px;
    color: #5e5c5c;
    padding-bottom: 15px;
  }
  img {
    float: right;
    width: 40%;
    margin-top:0;
  }
</style>