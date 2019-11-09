

function solution(n, lost, reserve) {
    var answer = 0;
    const arr = [];

    for(var i=1; i<=n; i++)
        arr[i] = 1;
    
    for(var i=0; i<reserve.length; i++)
        arr[reserve[i]]++;
    
    for(var i=0; i<lost.length; i++)
            arr[lost[i]]--;

    for(var i=1; i<arr.length-1; i++){
        if(arr[i] == 2 && arr[i+1] == 0){
            arr[i]--;
            arr[i+1]++;
        }
        else if(arr[i] == 0 && arr[i+1] == 2){
            arr[i]++;
            arr[i+1]--;
        }
    };
    
    for(var i=0; i<arr.length; i++)
        if(arr[i] >= 1) answer++;

    return answer;
}