<template>
	<div>
		<group title="cell demo">
			<cell title="abc" value="abc" is-link></cell>
		</group>
	</div>
</template>

<script>
	import { Group, Cell } from 'vux'
	export default {
		components: {
			Group,
			Cell
		},
		data () {
			return {
				msg: 'Hello World!'
			}
		},
		mounted() {
			this.$ajax.get('api/get_hello/').then((response) => {
				
			}).catch(function (error) {
				console.log(error);
			});
		}
	}
</script>

<style>
	.vux-demo {
		text-align: center;
	}
	.logo {
		width: 100px;
		height: 100px
	}
</style>
