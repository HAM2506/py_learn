<template>
	<div>
		<x-header :left-options="{showBack: false}">微信
			<span slot="right">
				<i class="iconfont icon-more" @click="showMore"></i>
			</span>
		</x-header>
		<group title="微信">
			<cell title="abc" value="abc" is-link></cell>
			<x-input title="用户名" v-model="value"></x-input>
		</group>
		<div class="more-menu">

		</div>
	</div>
</template>

<script>
	import { Group, Cell, XInput, XHeader } from 'vux'
	export default {
		components: {
			Group,
			Cell,
			XInput,
			XHeader
		},
		data () {
			return {
				msg: 'Hello World!',
				value: 123
			}
		},
		methods: {
			showMore() {
				console.info(0)
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

<style scoped>
	.vux-demo {
		text-align: center;
	}
	.logo {
		width: 100px;
		height: 100px
	}
	.iconfont {    
		font-size: 20px;
    	font-weight: bold;
	}
	.more-menu {
		position: absolute;
		top: 60px;
		right: 8px;
		width: 120px;
		height: 140px;
		background: #35495e;
	}
	.more-menu:before {
		content: '';
		position: absolute;
		top: -8px;
    	right: 14px;
		width: 0;
		height: 0;
		border-left: 8px solid transparent;
		border-right: 8px solid transparent;
		border-bottom: 10px solid #35495e;
	}
</style>
