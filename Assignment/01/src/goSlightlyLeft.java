import lejos.nxt.Button;
import lejos.nxt.LightSensor;
import lejos.nxt.Motor;
import lejos.nxt.SensorPort;
import lejos.robotics.navigation.DifferentialPilot;
import lejos.robotics.navigation.MoveController;
import lejos.util.Delay;

public class goSlightlyLeft {
	public static void main(String[] args) {
		double arcRad = 20;
		double angle = 90;
		double trackWidth = 12;
		Button.LEFT.waitForPressAndRelease();
		LightSensor lightSens1 = new LightSensor(SensorPort.S1);
		LightSensor lightSens2 = new LightSensor(SensorPort.S2);
		DifferentialPilot dp = new DifferentialPilot(MoveController.WHEEL_SIZE_NXT1, trackWidth, Motor.B, Motor.C, true);
		lightSens1.setHigh(100);
		lightSens2.setHigh(100);
		int loop;
		loop = 0;
		
		while(loop<=40){
			Button.LEFT.waitForPressAndRelease();
			Delay.msDelay(5000);
			dp.setTravelSpeed(10);
			dp.arc(-arcRad, angle);
			dp.stop();
			loop++;
		}
		Button.ESCAPE.waitForPressAndRelease();
	}
}