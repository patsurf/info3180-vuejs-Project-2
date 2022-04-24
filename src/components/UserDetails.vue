<template>
    <div class="profile-card row">
        <div class="column">
            <img :src="'/uploads/profile_photos/' + profile_image" alt="Profile Image" id="profile_image">  
        </div>
        <div class="column">
            <div>
                <ul class="profile-card-list">
                    <li>
                        <h2 class="profile-card-value">{{ name }}</h2>
                    </li>
                    <li>
                        <h5 class="profile-card-value">@{{ user_name }}</h5>
                    </li>
                    <li>
                        <p class="profile-card-value">{{ biography }}</p>
                    </li>
                    <li>
                        <p class="profile-card-key">Email<span class="profile-card-value">{{ email }}</span></p>
                    </li>
                    <li>
                        <p class="profile-card-key">Location<span class="profile-card-value">{{ location }}</span></p>
                    </li>
                    <li>
                        <p class="profile-card-key">Joined<span class="profile-card-value">{{ date_joined }}</span></p>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <br>
    <br>
    <div class="row">
        <h2>Favourites</h2>
        <div class="card-deck">
            <div v-for="car in Favourites" class="card">
               <img class="card-img-top" id="car_images" :src="'/uploads/car_photos/' + car.image" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">{{ car.year }} {{ car.make }}<button class="tags"><fa icon="tags"/> ${{ car.price }}</button></h5>
                    <p class="card-text" style="color:gray;">{{ car.model }}</p>
                    <button class=" View btn btn-primary"> <a id="id" :href="'/cars/' + car.id" >View more details</a></button>
                </div>
            </div>
        </div>
    </div>
    


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
            Favourites: [],
            make: '',
            model: '',
            year: '',
            price: '',
            image: '',
            id: '',
            favMessage: ''
        }
    },
    created() {
        this.getCsrfToken();
        this.getUserDetails();
        this.getFavouriteList();
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
        getFavouriteList() {
            let self = this;
            fetch("/api/users/" + sessionStorage.getItem("user_id") + "/favourites", {
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
                    self.favMessage = data.favMessage;
                    self.Favourites = data.allFavourites;
                    console.log("favourites: ", self.Favourites);
                    console.log("favMessage: ", self.favMessage);
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