package examples.exceptionsEx.autocloseable;

public class JammedTurkeyCage implements AutoCloseable {

	public void close() throws IllegalStateException {
		throw new IllegalStateException("Cage door does not close");
	}

	public static void catchExThrownByClose() {
		// catch an exception thrown by close():
		try (JammedTurkeyCage t = new JammedTurkeyCage()) {
			System.out.println("put turkeys in");
		} catch (IllegalStateException e) {
			System.out.println("caught: " + e.getMessage());
		} finally {
			System.out.println("finally");
		}
	}

	public static void catchPrimaryAndSuppressedExceptions() {
		try (JammedTurkeyCage t = new JammedTurkeyCage()) {
			throw new IllegalStateException("turkeys ran off");
		} catch (IllegalStateException e) {
			System.out.println("caught: " + e.getMessage());
			for (Throwable t : e.getSuppressed())
				System.out.println(t.getMessage());
		}
	}

	public static void noCatchForPrimaryAndSuppressedExceptions() {
		try (JammedTurkeyCage t = new JammedTurkeyCage()) {
			throw new RuntimeException("turkeys ran off");
		} catch (IllegalStateException e) {
			System.out.println("caught: " + e.getMessage());
		}
	}

	public static void looseExceptionsBecauseOfFinally() {
		try (JammedTurkeyCage t = new JammedTurkeyCage()) {
			throw new IllegalStateException("turkeys ran off");
		} finally {
			throw new RuntimeException("and we couldn't find them");
		}
	}

	public static void looseExceptionsBecauseOfCatch() {
		try (JammedTurkeyCage t = new JammedTurkeyCage()) {
			throw new IllegalStateException("turkeys ran off");
		} catch (IllegalStateException e) {
			throw new RuntimeException("and we couldn't find them");
		}
	}

	public static void twoExThrownWhenClosing() {
		try (JammedTurkeyCage t1 = new JammedTurkeyCage(); JammedTurkeyCage t2 = new JammedTurkeyCage(); JammedTurkeyCage t3 = new JammedTurkeyCage()) {
			System.out.println("turkeys entered cages");
		} catch (IllegalStateException e) {
			System.out.println("caught: " + e.getMessage());
			for (Throwable t : e.getSuppressed())
				System.out.println("TTT " + t.getMessage());
		}
	}

	public static void main(String[] args) {
		// catch an exception thrown by close()
//		 catchExThrownByClose();

		// first exception is the primary one and all other from try or close
		// are suppressed
//		 catchPrimaryAndSuppressedExceptions();

		// catch does not match primary ex
		// noCatchForPrimaryAndSuppressedExceptions();

		// what happens if two exceptions are thrown while closing resources
		 twoExThrownWhenClosing();

		// suppressed exceptions apply only to exceptions thrown in the try
		// clause or close
		// looseExceptionsBecauseOfFinally();
		// looseExceptionsBecauseOfCatch();
	}
}