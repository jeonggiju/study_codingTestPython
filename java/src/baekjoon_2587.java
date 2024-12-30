package src;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class baekjoon_2587 {
    private void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    private void quick(int[] arr, int start, int end){
        if(start >= end) return;

        int pivot = arr[start];
        int low = start+1;
        int high = end;

        while(low <= high){
            while(low <= end && arr[low] <= arr[pivot]){
                low++;
            }
            while(start < high && arr[pivot] >= arr[high]){
                high--;
            }

            if(low < high) {
                this.swap(arr, high, low);
            }else {
                this.swap(arr, pivot, high);
            }
        }

        quick(arr, start, high-1);
        quick(arr, high+1, end);
    }

    private void sort(int[] arr){
        quick(arr, 0, arr.length-1);
    }



    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> ls = new ArrayList<Integer>();

        for(int i = 0 ; i < 5 ; i++){

        }

    }

}
