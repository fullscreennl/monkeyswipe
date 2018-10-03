//
//  OOOStoreView.m
//  oneonone
//
//  Created by johan ten broeke on 3/26/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import "OOOStoreView.h"
#import "OOOStoreObserver.h"
#import <UIKit/UIKit.h>
#import "OOOReachability.h"

@implementation OOOStoreView

- (id)initWithFrame:(CGRect)frame {
	if ((self = [super initWithFrame:frame])) {
		isTrusted = NO;
		[self requestProductData];
	}
	return self;
}

- (void)alertView:(UIAlertView *)alertView clickedButtonAtIndex:(NSInteger)buttonIndex{
	
	if (isTrusted) {
		[[NSNotificationCenter defaultCenter] 
		 postNotification:[NSNotification 
						   notificationWithName:@"inAppPurchaseTransactionSuccess" 
						   object:self
						   userInfo:nil]];
		return;
	}
	
	//NSLog(@"alertview cancelled !");
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"inAppPurchaseTransactionFailed" 
					   object:self
					   userInfo:nil]];
		
}

- (void)dealloc {
	//[observer release];
	[warnDisabledAlert release];
	[reachability_obj release];
	[super dealloc];
}

- (void) requestProductData
{
	isTrusted = NO;
	[reachability_obj release];
	reachability_obj = [[OOOReachability alloc] init];
	if([reachability_obj isOnline] == 0){
		warnDisabledAlert = [[UIAlertView alloc] initWithTitle:@"Oops."
													   message:@"No internet connection."
													  delegate:self
											 cancelButtonTitle:@"OK"
											 otherButtonTitles:nil];
		[warnDisabledAlert show];
		return;
	}
	
	if([reachability_obj isOnline] == 2){
		warnDisabledAlert = [[UIAlertView alloc] initWithTitle:@"Yeah."
													   message:@"Your device is trusted by Appjuice go on and upgrade for free!"
													  delegate:self
											 cancelButtonTitle:@"OK"
											 otherButtonTitles:nil];
		isTrusted = YES;
		[warnDisabledAlert show];
		return;
	}
	
	if([reachability_obj isOnline] == 4){
		warnDisabledAlert = [[UIAlertView alloc] initWithTitle:@"Yeah."
													   message:@"Monkey Swipe is FREE for a limited time only, go on and upgrade for free!"
													  delegate:self
											 cancelButtonTitle:@"OK"
											 otherButtonTitles:nil];
		isTrusted = YES;
		[warnDisabledAlert show];
		return;
	}
	
	if ([SKPaymentQueue canMakePayments]){
		pay_request = [[SKProductsRequest alloc] initWithProductIdentifiers: [NSSet setWithObject: @"com.appjuice.MonkeySwipe.levelpack1"]];
		pay_request.delegate = self;
		[pay_request start];
	}else{
		//NSLog(@"In app purchases are disabled.!!");
		warnDisabledAlert = [[UIAlertView alloc] initWithTitle:@"Oops,in App purchases are disabled."
													   message:@"Please go to restrictions in your settings panel to enable in app purchases."
													  delegate:self
											 cancelButtonTitle:@"OK"
											 otherButtonTitles:nil];
		[warnDisabledAlert show];
	}
}

//***************************************
// PRAGMA_MARK: Delegate Methods
//***************************************
- (void)productsRequest:(SKProductsRequest *)request didReceiveResponse:(SKProductsResponse *)response
{
	NSArray *myProduct = response.products;
	for(int i=0;i<[myProduct count];i++)
	{
		SKProduct *product = [myProduct objectAtIndex:i];
		//NSLog(@"Name: %@ - Price: %f",[product localizedTitle],[[product price] doubleValue]);
		//NSLog(@"Product identifier: %@", [product productIdentifier]);
		SKPayment *payment = [SKPayment paymentWithProductIdentifier:[product productIdentifier]];
		if (observer == nil){ 
			observer = [OOOStoreObserver defaultStoreObserver];
			[[SKPaymentQueue defaultQueue] addTransactionObserver:observer];
		}
		[[SKPaymentQueue defaultQueue] addPayment:payment];
		//NSLog(@"current transactions : %@",[[SKPaymentQueue defaultQueue] transactions]);
	}
	[pay_request release];
}

@end

