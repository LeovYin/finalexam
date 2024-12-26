$(window).load(function () {
    $(".loading").fadeOut()
})
$(function () {
    echarts_21();
    echarts_22();
    echarts_23();
    echarts_4();
    function echarts_21() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart21'));

        option1 = {

            tooltip: {
                trigger: 'axis',
                axisPointer: { type: 'shadow' }
            },
            grid: {
                left: '0%',
                top: '10px',
                right: '0%',
                bottom: '0px',
                containLabel: true
            },
            xAxis: [{
                type: 'category',
                data: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                        width: 1,
                        type: "solid"
                    },
                },

                axisTick: {
                    show: false,
                },
                axisLabel: {
                    interval: 0,
                    // rotate:50,
                    show: true,
                    splitNumber: 15,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
            }],
            yAxis: [{
                type: 'value',
                axisLabel: {
                    //formatter: '{value} %'
                    show: true,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
                axisTick: {
                    show: false,
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1	)",
                        width: 1,
                        type: "solid"
                    },
                },
                splitLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                    }
                }
            }],
            series: [
                {
                    type: 'line',
                    data: [5030, 8600, 3000, 7200, 7200, 5130, 10030, 8600, 13000, 7200, 9130, 4130],

                    itemStyle: {
                        normal: {
                            color: '#37a3ff',
                            opacity: 1,

                            BorderRadius: 3,
                        }
                    }
                }
            ]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option1);
        window.addEventListener("resize", function () {
            myChart.resize();
        });


    }
    function echarts_22() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart22'));

        option1 = {
            //  backgroundColor: '#00265f',
            tooltip: {
                trigger: 'axis',
                axisPointer: { type: 'shadow' }
            },
            grid: {
                left: '0%',
                top: '5px',
                right: '0%',
                bottom: '0px',
                containLabel: true
            },
            xAxis: [{
                type: 'category',
                data: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                        width: 1,
                        type: "solid"
                    },
                },

                axisTick: {
                    show: false,
                },
                axisLabel: {
                    interval: 0,
                    // rotate:50,
                    show: true,
                    splitNumber: 15,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
            }],
            yAxis: [{

                type: 'value',
                axisLabel: {
                    //formatter: '{value} %'
                    show: true,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
                axisTick: {
                    show: false,
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1	)",
                        width: 1,
                        type: "solid"
                    },
                },
                splitLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                    }
                }
            }],
            series: [
                {
                    type: 'line',
                    data: [7200, 9130, 5030, 8600, 3000, 7200, 4130, 5130, 10030, 8600, 13000, 7200],

                    itemStyle: {
                        normal: {
                            color: '#37a3ff',
                            opacity: 1,
                            barBorderRadius: 3,
                        }
                    }
                }

            ]
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option1);
        window.addEventListener("resize", function () {
            myChart.resize();
        });

    }
    function echarts_23() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('feng01'));

        option1 = {
            //  backgroundColor: '#00265f',
            tooltip: {
                trigger: 'axis',
                axisPointer: { type: 'shadow' }
            },
            grid: {
                left: '0%',
                top: '5px',
                right: '0%',
                bottom: '0px',
                containLabel: true
            },
            xAxis: [{
                type: 'category',
                data: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                        width: 1,
                        type: "solid"
                    },
                },

                axisTick: {
                    show: false,
                },
                axisLabel: {
                    interval: 0,
                    // rotate:50,
                    show: true,
                    splitNumber: 15,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
            }],
            yAxis: [{

                type: 'value',
                axisLabel: {
                    //formatter: '{value} %'
                    show: true,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
                    },
                },
                axisTick: {
                    show: false,
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1	)",
                        width: 1,
                        type: "solid"
                    },
                },
                splitLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)",
                    }
                }
            }],
            series: [
                {
                    type: 'line',
                    data: [100, 86, 30, 72, 72, 51, 10, 86, 13, 72],
                    itemStyle: {
                        normal: {
                            color: '#37a3ff',
                            opacity: 1,
                            borderRadius: 3,
                        }
                    }
                },
                {
                    type: 'line',
                    data: [50, 60, 70, 80, 90, 100, 110, 120, 130, 140], // 添加第二条线的数据
                    itemStyle: {
                        normal: {
                            color: '#ff37a3', // 第二条线的颜色
                            opacity: 1,
                            borderRadius: 3,
                        }
                    }
                }
            ]
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option1);
        window.addEventListener("resize", function () {
            myChart.resize();
        });

    }



    function echarts_4() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart4'));

        option = {
            tooltip: {
                trigger: 'axis',
                axisPointer: { type: 'shadow' },
            }, "grid": {
                "top": "20%",
                "right": "50",
                "bottom": "20",
                "left": "30",
            },
            legend: {
                data: ['水位', '流量', '流速', '水温'],
                right: 'center', width: '100%',
                textStyle: {
                    color: "rgba(255,255,255,.5)"
                },
                itemWidth: 12,
                itemHeight: 10,
            },



            "xAxis": [
                {
                    "type": "category",
                    data: ['2016', '2017', '2018', '2019'],
                    axisLine: { show: false, },
                    axisLabel: {
                        textStyle: {
                            fontSize: 14,
                            color: "rgba(255,255,255,.5)",
                        },
                    },

                },
            ],
            "yAxis": [
                {

                    "type": "value",
                    // "name": "单位万",

                    axisTick: { show: false },
                    splitLine: { show: false, },
                    axisLine: { show: false, },
                    "axisLabel": {
                        "show": true,
                        fontSize: 14,
                        color: "rgba(255,255,255,.5)"

                    },
                    axisLine: {
                        min: 0,
                        max: 10,
                        show: false
                    },//左线色

                },
                {
                    "type": "value",
                    //"name": "增速",
                    "show": true,
                    "axisLabel": {
                        formatter: "{value} %",
                        fontSize: 14,
                        color: "rgba(255,255,255,.5)"
                    },
                    axisTick: { show: false },
                    splitNumber: 3,
                    axisLine: { show: false },//右线色
                    splitLine: { lineStyle: { color: 'rgba(255,255,255,.05)' } },//x轴线
                },
            ],
            "series": [

                {
                    "name": "水位",
                    "type": "bar",
                    "data": [36.6, 38.80, 40.84, 41.60],
                    "barWidth": "10%",
                    "itemStyle": {
                        "normal": {
                            barBorderRadius: 15,
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: '#8bd46e'
                            }, {
                                offset: 1,
                                color: '#09bcb7'
                            }]),
                        }
                    },
                    "barGap": "0.2"
                },
                {
                    "name": "流量",
                    "type": "bar",
                    "data": [14.8, 14.1, 15, 16.30],
                    "barWidth": "10%",
                    "itemStyle": {
                        "normal": {
                            barBorderRadius: 15,
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: '#248ff7'
                            }, {
                                offset: 1,
                                color: '#6851f1'
                            }]),
                        }
                    },
                    "barGap": "0.2"
                },
                {
                    "name": "流速",
                    "type": "bar",
                    "data": [9.2, 9.1, 9.85, 8.9],
                    "barWidth": "10%",
                    "itemStyle": {
                        "normal": {
                            barBorderRadius: 15,
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: '#fccb05'
                            }, {
                                offset: 1,
                                color: '#f5804d'
                            }]),
                        }
                    },
                    "barGap": "0.2"
                }
                ,
                {
                    "name": "水温",
                    "type": "line",
                    "yAxisIndex": 1,

                    "data": [3, 1, 5, 2.3],
                    lineStyle: {
                        normal: {
                            width: 2
                        },
                    },
                    "itemStyle": {
                        "normal": {
                            "color": "#3496f8",

                        }
                    },
                    //   "smooth": true,
                    symbolSize: 0,
                }
            ]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
    // function echarts_5() {
    //         // 基于准备好的dom，初始化echarts实例
    //         var myChart = echarts.init(document.getElementById('echart5'));

    //    var lightBlue = {
    // 	type: 'linear',
    // 	x: 0,
    // 	y: 0,
    // 	x2: 0,
    // 	y2: 1,
    // 	colorStops: [{
    // 		offset: 0,
    // 		color: 'rgba(41, 121, 255, 1)'
    // 	}, {
    // 		offset: 1,
    // 		color: 'rgba(0, 192, 255, 1)'
    // 	}],
    // 	globalCoord: false
    // }

    // var option = {
    // 	tooltip: {
    // 		show: false
    // 	},
    // 	grid: {
    // 		top: '0%',
    // 		left: '50',
    // 		right: '50',
    // 		bottom: '0%',
    // 	},
    // 	xAxis: {
    // 		min: 0,
    // 		//max: 12000,
    // 		splitLine: {
    // 			show: false
    // 		},
    // 		axisTick: {
    // 			show: false
    // 		},
    // 		axisLine: {
    // 			show: false

    // 		},
    // 		axisLabel: {
    // 			show: false
    // 		}
    // 	},
    // 	yAxis: {
    // 		data: ['数据','数据','数据','数据','数据','数据'],
    // 		//offset: 15,
    // 		axisTick: {
    // 			show: false
    // 		},
    // 		axisLine: {
    // 			show: false
    // 		},
    // 		axisLabel: {
    // 			color: 'rgba(255,255,255,.6)',
    // 			fontSize: 14,


    // 		}
    // 	},
    // 	series: [{
    // 		type: 'bar',
    // 		label: {
    // 			show: true,
    // 			zlevel: 10000,
    // 			position: 'right',
    // 			padding: 6,
    // 			color: '#4e84a1',
    // 			fontSize: 14,
    // 			formatter: '{c}'

    // 		},
    // 		itemStyle: {
    // 			  barBorderRadius: 25,
    // 			color:'#3facff'
    // 		},
    // 		barWidth: '15',

    // 		data: [ 1800, 1240, 1168, 1200, 2336, 1680],
    // 		z: 6
    // 	}
    // 		],
    // };


    //         // 使用刚指定的配置项和数据显示图表。
    //         myChart.setOption(option);
    //         window.addEventListener("resize",function(){
    //             myChart.resize();
    //         });
    // }





})


















