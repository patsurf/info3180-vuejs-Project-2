<script>
import CarForm from '@/components/CarForm.vue'
export default {
	data() {
	  return {
	  
	  };
	},
	components: { CarForm  }
};



</script>



<template>
		<div class="container">
			<CarForm></CarForm>
		</div>
    	
 



</template>


<style>

form { 
margin: 0 auto; 
width: 750px;
}

body {
    padding-top: 5rem;
    background-color: #f3f4f6;
}

label,input{
  display:flex;
  flex-direction:column;
}

/* style for actual form  */
[class*="form-row"]{
	border-radius: 10px;
    background-color: #ffffff;
    padding-top: 20px;
    padding-bottom: 20px;
    padding-left: 40px;
    width: 800px;
	
}

/* style for form fields */
[class*="form-group col-md-4"]{
	font-weight: bold;
	border-radius: 5px;
	display:inline-block;
	padding: 5px;
	width: 47%;
	gap: 10;
	
  	
}

[class*="btn btn-primary"]{
	background-color: rgb(45, 242, 140);
	border-color: rgb(45, 242, 140);
	width: 150px;
}

</style>