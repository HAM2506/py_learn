<template>
	<div class="topic-page">
		<x-header title="话题">
		</x-header>
        <div class="topic-wrap" v-for="(item, index) in topicList">
            <group :style="{height: item.height}">
                <cell class="topic-title" :title="item.topic_title"></cell>
                <cell class="topic-detail" :title="item.topic_detail"></cell>
                <cell class="topic-info">
					<flexbox slot="title">
						<flexbox-item>
							<div>{{ item.topic_time|time }}</div>
						</flexbox-item>
						<flexbox-item>
							<div>
								<input type="button" value="删除" class="delete" @click="deleteTopic(item.id, index)">
							</div>
						</flexbox-item>
					</flexbox>
				</cell>
            </group>
        </div>
		<confirm v-model="deleteTips" title="确定要删除吗？" @on-confirm="deleteConfirm"></confirm>
    	<toast v-model="successDelete" type="text" position="middle">删除成功</toast>
	</div>
</template>

<script>
	import { XTextarea, Group, XInput, XHeader, Toast, Cell, Flexbox, FlexboxItem, Confirm } from 'vux'
	import Time from '../utils/time.js'
	const T = new Time();
	export default {
		components: {
			XTextarea,
			Group,
			XInput,
			XHeader,
			Toast,
            Cell,
			Flexbox,
			FlexboxItem,
			Confirm
		},
		data () {
			return {
                topicList: [],
				deleteTips: false,
				topicId: 0,
				topicIndex: 0,
				successDelete: false
			}
		},
		methods: {
            deleteTopic(id, i) {
				this.deleteTips = true;
				this.topicId = id;
				this.topicIndex = i;
			},
			deleteConfirm() {
				this.topicList[this.topicIndex].height = 0;
				// this.$ajax.get('api/delete_topic/', {
				// 	params: { id: this.topicId }
				// }).then((res) => {
				// 	this.topicList.splice(this.topicIndex, 1);
				// 	this.successDelete = true;
				// }).catch((error) => {
				// 	console.log(error);
				// });
			}
		},
		mounted() {
			this.$ajax.get('api/get_topic/').then((res) => {
                this.topicList = [ ...res.data.data ].reverse();
				this.$nextTick(() => {
					this.topicList.forEach((item, index) => {
						this.topicList[index].height = document.getElementsByClassName('weui-cells')[index].offsetHeight + 'px';
					}) 
				})
			}).catch((error) => {
				console.log(error);
			});
		},
		watch: {
            
		}
	}
</script>

<style>
    .topic-page .weui-cell:before {
        display: none;
    }
    .topic-page .topic-title {
        font-size: 18px;
    }
    .topic-page .topic-detail {
        font-size: 14px;
		padding: 0 15px;
        color: #adadad;
    }
	.topic-page .topic-detail .vux-label {
		overflow: hidden;
		text-overflow: ellipsis;
		display: -webkit-box;
		-webkit-line-clamp: 2;
		-webkit-box-orient: vertical;
	}
    .topic-page .topic-info {
        font-size: 12px;
        color: #adadad; 
    }
	.topic-page .delete { 
		border: none;
		width: 40px;
		height: 20px;
		background: #fff;
		color: #35495e;
		font-size: 12px;
    	text-decoration: underline;
		float: right;
	}
</style>
