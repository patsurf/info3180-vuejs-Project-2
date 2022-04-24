<template>
    <div class="container">
        <UserDetails></UserDetails>
    </div>
</template>
<script>
    import UserDetails from '@/components/UserDetails.vue'
    export default {
        data() {
            return {};
        },
        components: { UserDetails  }
    }
</script>
<style>

body{
    background-color:  #ececec;
}
.container{
    margin: 0 auto;
    width: 900px;
    /* background-color: #ffffff; */
    border-radius: 10px;
    padding: 25px;
    /* width: 800px; */
}
.column {
    flex: 40%;
    padding: 10px;
}
.row {
    display:flex;
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

[class*="profile-card"]{
    background-color: #ffffff;
	border-radius: 15px;
	padding: 10px;    
}

[class*="profile-card-list"]{
    list-style: none;
}

.profile-card-list li{
    margin-top: -10px;
    margin-bottom: -10px;
}

h5{
    font-size: 20px;
    font-weight: bold;
    color: gray;
    margin-top: -15px;
}

.profile-card-key{
    font-weight: bold;
    color: gray;
}

.profile-card-key span{
    font-weight: bold;
    color: black;
}


[id*="profile_image"]{
    float: left;
}

.card-deck {
    display: flex;
    /* flex-flow: row wrap; */
    justify-content: center;
    align-items: center;
    margin: 0 auto;
    
    
}
.card{
    width: 40%;
    border-radius: 20px;

    margin: 10px;
    box-shadow: 2px 2px 10px gray;
}
.card-deck img {
    width: 100%;
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

</style>