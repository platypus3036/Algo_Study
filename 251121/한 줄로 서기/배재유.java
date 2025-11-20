import java.io.*;
import java.util.*;





public class Main {
	
	public static class Node {
		int data;
		Node prev;
		Node next;
		
		public Node(int data) {
			this.data = data;
			this.prev = null;
			this.next = null;
		}
	}
	
	
	public static class DoublyLinkedList {
		Node tail;
		Node head;
		
		//생성자는 아예 head, tail초기화로 처리
		public DoublyLinkedList() {
			this.head = null;
			this.tail = null;
		}
		
		
		public void add(int data) {
			Node newNode = getNewNode(data);
			
			if(head == null) {
				head = newNode;
				tail = newNode;
				return;
			}
			
			tail.next = newNode;
			newNode.prev = tail;
			tail = newNode;
			
		}

	}
	
	public static int MAX_LENGTH = 0;
	public static Node[] nodePool = new Node[MAX_LENGTH];
	public static int nodeCnt = 0;
	
	
	public static Node getNewNode(int data) {
		
		if(nodePool[nodeCnt] == null) {
			nodePool[nodeCnt] = new Node(0);
		}
		
		//node로 채웟으니 이제 다시 해당 노드를 채워야한다
		
		Node node = nodePool[nodeCnt];
		node.data = data;
		node.prev = null;
		node.next = null;
		
		nodeCnt++;
		
		return node;

	}
	
	
	public static Node getNode(int index, DoublyLinkedList list) {
		int cnt = 0;
		Node node = list.tail;
		while(cnt < index) {
			cnt++;
			node = node.next;
		}
		
		return node;

		
	}
	
	public static void init(DoublyLinkedList list) {
		list.tail = null;
		list.head = null;
		nodeCnt = 0;
	}
 	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		/*
		 * 
		 * 줄을 어떻게 서야하는지
		 * 
		 * 사람들은 자기보다 큰사람이 왼쪽에 몇명있는지만 기억한다
		 * 
		 * 입력에서 주어지는건
		 * 
		 * i=1 부터 자기보다 큰 사람 수
		 * 0-idx
		 * 
		 * 나보다 큰 사람을 안다 = 최소 idx가 보장
		 * 4 2 1  3
		 *  
		 * 역순으로 돌리면서 나보다 큰 개수의 까지 index 해서 
		 * LinkedList      
		 * 
		 * 이거 LinkedList 안해도 되는게 N <= 10이다
		 * 그냥 배열 조작이 훨씬 빠르다
		 *       
		 *         
		 * 
		 * */
		int N = Integer.parseInt(br.readLine());
		
		int[] arr = new int[N+1];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 1; i<=N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		List<Integer> list = new ArrayList<>();
		
//		DoublyLinkedList list = new DoublyLinkedList();
		for(int i = N; i>0; i--) {
			int cnt = arr[i];
			list.add(cnt,i);
		}
		StringBuilder sb=  new StringBuilder();
		for(int i = 0; i<list.size(); i++) {
			sb.append(list.get(i)+" ");
		}
		
		bw.write(sb.toString().trim());
		bw.flush();
		bw.close();
		
		
		
		}
		
}
