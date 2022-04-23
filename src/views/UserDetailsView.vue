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

[class*="profile-card"]{
    background-color: #ffffff;
	border-radius: 5px;
	padding: 10px;
    height: ;
    
    
}

[class*="profile-card"]{
    list-style: none;
}

[id*="profile_image"]{
    float: left;
}

</style>