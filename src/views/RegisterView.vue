<script>
import RegisterForm from '@/components/RegisterForm.vue'
export default {
	data() {
	  return {
	  
	  };
	},
	components: { RegisterForm  }
};


</script>



<template>
		<div class="container">
    	 <RegisterForm></RegisterForm>
		</div>
 

</template>




<style>

form { 
	margin: 0 auto; 
	width: 750px;
	background-color: #ffffff;
	border-radius: 10px;
    padding-top: 20px;
    padding-bottom: 20px;
    padding-left: 40px;
    width: 800px;
}

body {
    padding-top: 5rem;
    background-color: #ececec;
}


/* style for form fields */
[class*="form-group"]{
	font-weight: bold;
	border-radius: 5px;
	display:inline-block;
	padding: 5px;
	width: 47%;
	
	
  	
}

[class*="form-groupbio"]{
	margin-right: 50px;
	
}

[class*="btn btn-lg btn-primary"]{
	background-color: rgb(45, 242, 140);
	border-color: rgb(45, 242, 140);
	width: 150px;
	
}

</style>