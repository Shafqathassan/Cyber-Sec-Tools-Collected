//From GeeksForGeeks
//https://www.geeksforgeeks.org/sha-256-hash-in-java/
//SHA 256 algorithm, is one of the most widely used hash algorithms. While there are other variants, SHA 256 has been at the forefront of real-world applications.

	import java.math.BigInteger;
//NIO was developed to allow Java programmers to implement high-speed I/O without using the custom native code. 
//for more details on NIO visit : https://docs.oracle.com/javase/8/docs/api/java/nio/package-summary.html
	import java.nio.charset.StandardCharsets;
//Message digests are secure one-way hash functions that take arbitrary-sized data and output a fixed-length hash value.
	import java.security.MessageDigest;
//This exception is thrown when a particular cryptographic algorithm is requested but is not available in the environment.
	import java.security.NoSuchAlgorithmException;

// Java program to calculate SHA hash value

	class GFG2 {
		public static byte[] getSHA(String input) throws NoSuchAlgorithmException
		{
		// Static getInstance method is called with hashing SHA
			MessageDigest md = MessageDigest.getInstance("SHA-256");

		// digest() method called
		// to calculate message digest of an input
		// and return array of byte
			return md.digest(input.getBytes(StandardCharsets.UTF_8));
		}
	
		public static String toHexString(byte[] hash)
		{
		// Convert byte array into signum representation
			BigInteger number = new BigInteger(1, hash);

		// Convert message digest into hex value
			StringBuilder hexString = new StringBuilder(number.toString(16));

		// Pad with leading zeros
			while (hexString.length() < 64)
			{
				hexString.insert(0, '0');
			}

			return hexString.toString();
		}	

	// Driver code
		public static void main(String args[])
		{
			try
			{	
				System.out.println("HashCode Generated by SHA-256 for:");

				String s1 = "GeeksForGeeks";
				System.out.println("\n" + s1 + " : " + toHexString(getSHA(s1)));
	
				String s2 = "hello world";
				System.out.println("\n" + s2 + " : " + toHexString(getSHA(s2)));
			
				String s3 = "K1t4fo0V";
				System.out.println("\n" + s3 + " : " + toHexString(getSHA(s3)));
			}
	// For specifying wrong message digest algorithms
			catch (NoSuchAlgorithmException e) {
				System.out.println("Exception thrown for incorrect algorithm: " + e);
			}
		}
	}
