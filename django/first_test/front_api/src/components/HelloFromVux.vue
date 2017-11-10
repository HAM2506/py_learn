<template>
	<div>
		<x-header :left-options="{showBack: false}">
			<div slot="right">
				<input type="button" value="发表" class="send" :class="{ 'send-light' : isButtonLight }" @click="sendTopic">
			</div>
		</x-header>
		<div class="topic-board">
			<group>
				<x-input placeholder="标题" v-model="sendInfo.title"></x-input>
				<x-textarea :max="200" placeholder="内容" v-model="sendInfo.detail"></x-textarea>
			</group>
		</div>
    	<toast v-model="successToast" type="text" position="middle">发表成功</toast>
	</div>
</template>

<script>
	import { XTextarea, Group, XInput, XHeader, Toast } from 'vux'
	export default {
		components: {
			XTextarea,
			Group,
			XInput,
			XHeader,
			Toast
		},
		data () {
			return {
				sendInfo: {
					title: '',
					detail: ''
				},
				isButtonLight: false,
				successToast: false
			}
		},
		methods: {
			sendTopic() {
				if (!this.isButtonLight) return;
				this.sendInfo.time = Date.parse(new Date());
				this.$ajax.get('api/save_topic/',{
					params: this.sendInfo
				}).then((response) => {
					this.successToast = true;
					this.sendInfo = {
						title: '',
						detail: ''
					}
					this.$router.push({ name: 'topic' })
				}).catch(function (error) {
					console.log(error);
				});
				console.log(this.sendInfo)
			}
		},
		mounted() {
			console.log(this)
			this.$ajax.get('api/get_topic/').then((response) => {
				
			}).catch(function (error) {
				console.log(error);
			});
		},
		watch: {
			sendInfo: {
				deep: true,
				handler: function(val) {
					val.title && val.detail ? this.isButtonLight = true : this.isButtonLight = false;
				}
			}
		}
	}
</script>

<style>
	.topic-board .weui-cells {
		margin-top: 0px;
	}
	.topic-board textarea {
		font-family: inherit;
	}
	.send {
		border: none;
		width: 40px;
		height: 20px;
		background: #35495e;
		color: green;
		font-size: 14px;
		vertical-align: top;
	}
	.send-light {
		color: #01e701;
	}
	.topic-board .weui-cell:before {
		right: 15px;
	}
</style>
