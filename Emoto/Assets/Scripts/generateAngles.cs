using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.IO;
using UnityEngine;
using UnityEditor;

public class generateAngles : MonoBehaviour {
	public bool recordingMoves = false;

	//possible other method is having a list of names, list of game objects, list of springs, list of anglelists
	private Dictionary<string, List<float>> emotoAngles = new Dictionary<string, List<float>>();

	public GameObject phone;
	public GameObject neck;
	public GameObject wrist;
	public GameObject elbow;
	public GameObject shoulder;
	public GameObject foot;

	private HingeJoint phoneHinge;
	private JointSpring phoneHingeSpring;
	private List<float> phoneAngles = new List<float>();

	private HingeJoint neckHinge;
	private JointSpring neckHingeSpring;
	private List<float> neckAngles = new List<float>();

	private HingeJoint wristHinge;
	private JointSpring wristHingeSpring;
	private List<float> wristAngles = new List<float>();

	private HingeJoint elbowHinge;
	private JointSpring elbowHingeSpring;
	private List<float> elbowAngles = new List<float>();

	private HingeJoint shoulderHinge;
	private JointSpring shoulderHingeSpring;
	private List<float> shoulderAngles = new List<float>();

	private HingeJoint footHinge;
	private JointSpring footHingeSpring;
	private List<float> footAngles = new List<float>();

	public int physicalFrameRate = 1;
	// Use this for initialization
	void Start () {
		//grabbing the hinge component, making sure the setting is on spring
		phoneHinge = phone.GetComponent<HingeJoint>();
		phoneHinge.useSpring = true;
		//phoneHingeSpring = phoneHinge.spring;

		neckHinge = neck.GetComponent<HingeJoint>();
		neckHinge.useSpring = true;
		//neckHingeSpring = neckHinge.spring;

		wristHinge = wrist.GetComponent<HingeJoint>();
		wristHinge.useSpring = true;
		//wristHingeSpring = wristHinge.spring;

		elbowHinge = elbow.GetComponent<HingeJoint>();
		elbowHinge.useSpring = true;
		//elbowHingeSpring = elbowHinge.spring;

		shoulderHinge = shoulder.GetComponent<HingeJoint>();
		shoulderHinge.useSpring = true;
		//shoulderHingeSpring = shoulderHinge.spring;

		footHinge = foot.GetComponent<HingeJoint>();
		footHinge.useSpring = true;
		//footHingeSpring = footHinge.spring;
	}
	
	// Update is called once per frame
	void Update () {
		if (recordingMoves) {
			phoneAngles.Add (Mathf.Abs(phoneHinge.angle));
			neckAngles.Add (Mathf.Abs(neckHinge.angle));
			wristAngles.Add (Mathf.Abs(wristHinge.angle));
			elbowAngles.Add (Mathf.Abs(elbowHinge.angle));
			shoulderAngles.Add (Mathf.Abs(shoulderHinge.angle));
			footAngles.Add (Mathf.Abs(footHinge.angle));
		}
	}
	public void onOffRecord (bool recording){//event listener for the next time the button is pressed and when recording becomes false
		recordingMoves = recording;
		if (recordingMoves) {
			//take all lists and put them into dictionary with values
			emotoAngles.Add("phone",phoneAngles);
			emotoAngles.Add("neck",neckAngles);
			emotoAngles.Add("wrist",wristAngles);
			emotoAngles.Add("elbow",elbowAngles);
			emotoAngles.Add("shoulder",shoulderAngles);
			emotoAngles.Add("foot",footAngles);
		}
		else {
			OutputMovement (emotoAngles);	
			emotoAngles.Clear();
		}
	}

	[MenuItem("Tools/Write file")]

	public static void OutputMovement (Dictionary<string, List<float>> emotoAngles) {
		const string fileName = "movements.txt";
		string path = "Assets/Scripts/movements.txt";
		StreamWriter writer = new StreamWriter (path, true);
		writer.WriteLine("dictionary = {");
		foreach (KeyValuePair<string, List<float>> attachStat in emotoAngles) {
			StringBuilder str = new StringBuilder ();//string of all the angles
			foreach (float angle in attachStat.Value) {
				string angleAdd = angle.ToString ("F1");//trying to truncate float at 1 decimal point
				str.Append(angleAdd);
				str.Append(',');
			}
			writer.WriteLine("'"+attachStat.Key+"' : ["+str+"]");
		}
		writer.WriteLine ("}");
		writer.Close ();
	}
}
