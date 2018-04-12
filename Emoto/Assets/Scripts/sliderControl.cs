using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
//this is the script added to each joint to allow for the hinge component to be controlled by a slider
public class sliderControl : MonoBehaviour {
	
	private HingeJoint hinge;
	private JointSpring hingeSpring;
	public int springForce = 80;
	public int dampForce = 40;
	public float startingAngle = 100;

	private float targetAngle = 100;


	//public string nameOfJoint = "name of joint";
	//public bool printAngle = False;

	void Start () {
		hinge = gameObject.GetComponent<HingeJoint>();
		hingeSpring = hinge.spring;
		targetAngle = startingAngle;
		hinge.useSpring = true;
	}
	
	// Update is called once per frame
	void Update () {
		hinge.useSpring = true;
		hingeSpring.targetPosition = targetAngle;
	}
	public void ChangeAngles (float newAngle) {
		//hinge = gameObject.GetComponent<HingeJoint>();

		hingeSpring.spring = springForce;
		hingeSpring.damper = dampForce;
		targetAngle = newAngle;
//		print (hingeSpring.targetPosition);

		hinge.spring = hingeSpring;
	}
}

