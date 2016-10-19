import lejos.nxt.LightSensor;
import lejos.nxt.Motor;
import lejos.nxt.SensorPort;
import lejos.robotics.navigation.DifferentialPilot;
import lejos.robotics.navigation.MoveController;
import lejos.util.Delay;
import lejos.nxt.Button;

public class goStraight {

	public static void main(String[] args) {
		double arcRad = 40;
		double angle = 90;
		double arcLen = Math.PI*2*arcRad*angle/360;
		double trackWidth = 12;
		int loop;
		loop = 0;
		LightSensor lightSens1 = new LightSensor(SensorPort.S1);
		LightSensor lightSens2 = new LightSensor(SensorPort.S2);
		DifferentialPilot dp = new DifferentialPilot(MoveController.WHEEL_SIZE_NXT1, trackWidth, Motor.B, Motor.C, true);
		lightSens1.setHigh(100);
		lightSens2.setHigh(100);
		
		while(loop <= 40){
			Button.LEFT.waitForPressAndRelease();
			Delay.msDelay(5000);
			dp.setTravelSpeed(10);
			dp.travel(-arcLen);        
			dp.stop();
			loop++;
		}
		Button.ESCAPE.waitForPressAndRelease();
	}
}