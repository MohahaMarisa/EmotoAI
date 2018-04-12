using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class textHandler : MonoBehaviour {
	const string fileName = "movements.txt";
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}

	public void OutputMovement () {
		using (BinaryWriter writer = new BinaryWriter (File.Open (fileName, FileMode.Create))) {
			writer.Write (123);
			writer.Write (123.456f);
			writer.Write ("Hello, World!");
			writer.Write(true);
		}
	}
}
