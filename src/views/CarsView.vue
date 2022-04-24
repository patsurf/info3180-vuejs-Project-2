<template>
    <div class="container">
        <ExploreCars></ExploreCars>
    </div>
</template>
<script>
import ExploreCars from "../components/ExploreCars.vue";
export default {
    data() {
        return {};
    },
    components: {
        ExploreCars
    }
}


</script>

<style>

#CarSearchForm { 
    margin: 0 auto; 
    width: 750px;
    box-shadow: 2px 2px 10px gray;
    display: inline-block;
    background-color: white;
    border-radius: 10px;
    padding: 10px;
}
.View{
    width: 100%;
    padding: 10px;
    font-size: 16px;
    font-weight: bold;
}
#id{
    color: white;
    text-decoration: none;
}
.card-deck {
    display: flex;
    /* flex-flow: row wrap; */
    justify-content: center;
    align-items: center;
    /* margin: 0 auto; */
    
    
}
.card{
    width: 500px;
    border-radius: 10px;

    margin: 10px;
    box-shadow: 2px 2px 10px gray;
}
.card-deck img {
    width: 100%;
}
#CarSearchForm .form-group{
    width: 40%;
    font-weight: bold;
}

.tags {
    padding:5px;
    margin-left: 15px;
    border-radius: 10px;
    border: 1px solid #0fb881;
    background-color: #0fb881;
    color: white;
    float: right;
}
.card-title{
    display: inline;
    margin-bottom: 15px;
}

.card-text{
     margin-top: 10px;
     padding-bottom: 30px;
}

/* body{
    background-color: #f3f4f6;
    display: flex;
    justify-content: center;
    align-items: center;
}



[class*="form"]{
    display: inline-block;
    background-color: white;
    border-radius: 10px;
    padding: 10px;
}



[class*="btn btn-primary"]{
    background-color: rgb(45, 242, 140);
	border-color: rgb(45, 242, 140);
    position: relative;
    width: 132px;
    top: -52px;
    left: 590px;
    
}
 */

</style>