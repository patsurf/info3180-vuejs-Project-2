<template>
    <div>
       <h2>Username </h2> {{user_name}}
    </div>
    <div>
        <h2>Name </h2>{{name}}
    </div>
    <div>
        <h2>Email </h2>{{email}}
    </div>
    <div>
        <h2>Location </h2>{{location}}
    </div>
    <div>
        <h2>Biography </h2>{{biography}}
    </div>
    <div>
        <h2>Date Joined </h2>{{date_joined}}
    </div>
        <img :src="'/uploads/profile_photos/' + profile_image" alt="Profile Image" id="profile_image">


</template>
<script>
import router from "../router";
import store from '@/main.js'; 

export default {
    data(){
        return {
            name: '',
            user_name: '',
            user_id: '',
            email: '',
            location: '',
            biography: '',
            date_joined: '',
            profile_image: '',
        }
    },
    created() {
        this.getCsrfToken();
        this.getUserDetails();
    },

    methods: {
         getCsrfToken() {
            let self = this;
            fetch("/api/csrf-token")
                .then((response) => {
                    return response.json();
                })
                .then((data) => {
                    console.log(data);
                    self.csrfToken = data.csrf_token;
                });
        },
        getUserDetails() {
            let self = this;
            fetch("/api/users/" + sessionStorage.getItem("user_id"), {
                method: "GET",
                headers: {
                    'X-CSRF-TOKEN': this.csrf_token,
                    'Authorization': 'Bearer ' + sessionStorage.getItem('token')
                }
            })
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) {
                    self.message = data.message;
                    self.user_id = data.user_id;
                    self.name = data.name;
                    self.user_name = data.username;
                    self.email = data.email;
                    self.location = data.location;
                    self.biography = data.biography;
                    self.date_joined = data.date_joined;
                    self.profile_image = data.profile_img;
                    console.log("user_id: ", self.user_id);
                    console.log("user_name: ", self.user_name);
                    console.log("email: ", self.email);
                    console.log("location: ", self.location);
                    console.log("biography: ", self.biography);
                    console.log("date_joined: ", self.date_joined);
                    // console.log("profile_image: ", self.profile_image);
                })
                .catch(function (error) {
                    console.log(error);
                });
        },
    }
}


</script>
<style>
    #profile_image {
        width: 200px;
        height: 200px;
        border-radius: 50%;
    }
</style>