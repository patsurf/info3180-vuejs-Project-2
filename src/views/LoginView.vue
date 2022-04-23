<script>
import LoginForm from '@/components/LoginForm.vue'
export default {
	data() {
	  return {
	  
	  };
	},
	components: { LoginForm  }
};



</script>



<template>
	<div class="container">
    	 <LoginForm></LoginForm>
	</div>

</template>


<style>

body{
    background-color: #ececec;
    display: flex;
    justify-content: center;
    align-items: center;
	height: 600px;
}

form { 
	margin: 0 auto; 
	box-shadow: 5px 5px 5px gray;
}

[class*="form-signin"]{
	background-color: #ffffff;
	border-radius: 5px;
	padding: 10px;
}

[class*="form-group col-md-4"]{
	width: 270px;
}

[class*="sr-only"]{
	font-weight: bold;
}

[class*="btn btn-lg btn-primary"]{
	background-color: rgb(45, 242, 140);
	border-color: rgb(45, 242, 140);
	width: auto;
}

</style>