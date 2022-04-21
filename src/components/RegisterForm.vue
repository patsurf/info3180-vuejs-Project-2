<template>
<form id= "registerForm" @submit.prevent="uploadPhoto" enctype="multipart/form-data">

<label for="username"> Username</label>
<p> Please provide a username</p>
<input type="text"/><br>

<label for="password">Password</label>
<p> Please provide a password</p>
<input type="text"/><br>

<label for="email"> Email</label>
<p>Please provide an email address</p>
<input type="text"/><br>

<label for="name">Name</label>
<p>Please provide a Name</p>
<input type="text"/><br>


<label for="location">Address</label>
<p>Please provide your home address</p>
<input type="text"/><br>


<label for="biography">Biography</label>
<p>Please provide a brief biography</p>
<input type="text"/><br>


<label for="photo">Photo</label>
<p>Upload your photo</p>
<br><input type="file" name="photo"/><br>


<br><label for="date_joined">Date Joined</label>
<p>Please enter the date you joined</p>
<input type="date" name="date_joined"/><br>

<br><button type="submit"   value="register"> Register</button>


</form>

</template>


<script>
export default{
 data(){
  return {
     csrf_token:''
  }
 },

 created(){
    this.getCsrfToken();
 },

methods:{

  uploadPhoto() {
    let self= this;
    let registerForm= document.getElementById('registerForm');
    let form_data = new FormData(registerForm);
   fetch("/api/register", {
      method: 'POST',
      body:form_data,
      headers:{
         'X-CSRFToken': this.csrf_token
      }
   })

   .then(function(response){
   	  return response.json();
   })
   .then(function (data){
     console.log(data);
   })
   .catch(function (error){
     console.log(error);
   });

  },
  getCsrfToken() {
   let self=this;
   fetch('/api/csrf-token')
     .then((response) => response.json())
     .then((data) => {
       console.log(data);
         self.csrf_token = data.csrf_token;
     })
  }
	
 }
};



</script>


