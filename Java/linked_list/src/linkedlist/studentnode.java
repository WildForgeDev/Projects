package linkedlist;

public class studentnode {
	//data
	public int data;
	//pointer to next node
	public studentnode next;
	
	public studentnode(int data, studentnode next) {
	this.data = data;
	this.next = next;
}

public String toString() {
	return data + "";
	}
}
