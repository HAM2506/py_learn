<template>
	<div class="topicPage">
        <div class="topicWrap" v-for="item in topicList">
            <group>
                <cell class="topicTitle" :title="item.topic_title"></cell>
                <cell class="topicDetail" :title="item.topic_detail"></cell>
                <cell class="topicInfo" :title="item.topic_time"></cell>
            </group>
        </div>
	</div>
</template>

<script>
	import { XTextarea, Group, XInput, XHeader, Toast, Cell } from 'vux'
	export default {
		components: {
			XTextarea,
			Group,
			XInput,
			XHeader,
			Toast,
            Cell
		},
		data () {
			return {
                topicList: []
			}
		},
		methods: {
            
		},
		mounted() {
			this.$ajax.get('api/get_topic/').then((res) => {
                this.topicList = [ ...res.data.data ];
				console.log(this.topicList)
			}).catch(function (error) {
				console.log(error);
			});
		},
		watch: {
            
		}
	}
</script>

<style>
    .topicPage .weui-cell:before {
        display: none;
    }
    .topicPage .topicTitle {
        font-size: 18px;
    }
    .topicPage .topicDetail {
        font-size: 16px;
        color: #adadad;
    }
    .topicPage .topicInfo {
        font-size: 12px;
        color: #adadad; 
    }
</style>
