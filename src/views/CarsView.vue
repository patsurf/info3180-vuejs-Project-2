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

body{
    background-color: #f3f4f6;
    display: flex;
    justify-content: center;
    align-items: center;
}

form { 
    margin: 0 auto; 
    width: 750px;
    box-shadow: 2px 2px 10px gray;
}

[class*="form"]{
    display: inline-block;
    background-color: white;
    border-radius: 10px;
    padding: 10px;
}

[class*="form-group col-md-4"]{
    width: 40%;
    font-weight: bold;
}

[class*="btn btn-primary"]{
    background-color: rgb(45, 242, 140);
	border-color: rgb(45, 242, 140);
    position: relative;
    width: 132px;
    top: -52px;
    left: 590px;
    
}

[class*="card-deck"]{
    


}

</style>