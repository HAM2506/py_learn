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
	</div>
</template>

<script>
	import { XTextarea, Group, XInput, XHeader } from 'vux'
	export default {
		components: {
			XTextarea,
			Group,
			XInput,
			XHeader
		},
		data () {
			return {
				sendInfo: {
					title: '',
					detail: ''
				},
				isButtonLight: false
			}
		},
		methods: {
			sendTopic() {
				if (!this.isButtonLight) return;
				this.sendInfo.time = Date.parse(new Date());
				this.$ajax.get('api/save_topic/',{
					params: this.sendInfo
				}).then((response) => {
					
				}).catch(function (error) {
					console.log(error);
				});
				console.log(this.sendInfo)
			}
		},
		mounted() {
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
</style>
